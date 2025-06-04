terraform {
  required_providers {
    huaweicloud = {
      source = "huaweicloud/huaweicloud"
      version = "~> 1.0"
    }
  }
}

provider "huaweicloud" {
  region     = var.region
  access_key = var.access_key
  secret_key = var.secret_key
}

# VPC Kaynağı
resource "huaweicloud_vpc" "vpc" {
  name = var.vpc_name
  cidr = var.vpc_cidr
}

# ECS Kaynağı
resource "huaweicloud_compute_instance" "ecs" {
  name              = var.ecs_name
  image_id          = var.image_id
  flavor_id         = var.flavor
  security_groups   = [huaweicloud_networking_secgroup.sg.name]
  availability_zone = var.availability_zone
  key_pair          = var.key_pair

  network {
    uuid = huaweicloud_vpc.vpc.id
  }
}

# Güvenlik Grubu Kaynağı
resource "huaweicloud_networking_secgroup" "sg" {
  count       = var.create_security_group ? 1 : 0
  name        = var.security_group_name
  description = var.description
  vpc_id      = var.vpc_id
}

# Güvenlik Grubu Kuralları
resource "huaweicloud_networking_secgroup_rule" "sg_rule" {
  count             = var.create_security_group_rule ? 1 : 0
  security_group_id = var.security_group_id
  direction         = var.direction
  protocol          = var.protocol
  port_range_min    = var.port_range_min
  port_range_max    = var.port_range_max
  remote_ip_prefix  = var.remote_ip_prefix
}

# RDS Kaynağı
resource "huaweicloud_rds_instance" "rds" {
  count   = var.create_rds ? 1 : 0
  name    = var.rds_name
  engine  = var.engine
  version = var.version
}

# RDS Yedekleme
resource "huaweicloud_rds_backup" "backup" {
  instance_id = huaweicloud_rds_instance.rds.id
  name        = var.backup_name
}

# OBS Bucket
resource "huaweicloud_obs_bucket" "bucket" {
  count         = var.create_obs ? 1 : 0
  bucket        = var.bucket_name
  storage_class = var.storage_class
  versioning    = var.versioning
}

# OBS Object
resource "huaweicloud_obs_bucket_object" "object" {
  bucket = huaweicloud_obs_bucket.bucket.bucket
  key    = var.object_key
  source = var.file_path
}

# IMS Image
resource "huaweicloud_images_image" "image" {
  name        = var.image_name
  instance_id = var.ecs_id
  description = var.description
  image_type  = var.image_type
  min_disk    = var.min_disk
  min_ram     = var.min_ram
  tags        = var.tags
}

# IMS Image Paylaşımı
resource "huaweicloud_images_image_member" "member" {
  image_id    = huaweicloud_images_image.image.id
  project_id  = var.project_id
  share_type  = var.share_type
  duration    = var.share_duration
}

# IMS Image Kopyalama
resource "huaweicloud_images_image_copy" "copy" {
  source_image_id = var.source_image_id
  target_region   = var.target_region
  name            = var.target_image_name
  copy_type       = var.copy_type
}

# IMS Image Versiyonlama
resource "huaweicloud_images_image_version" "version" {
  image_id    = huaweicloud_images_image.image.id
  name        = var.version_name
  description = var.version_description
  protected   = var.is_protected
}

# IMS Image Şablonu
resource "huaweicloud_images_image_template" "template" {
  name        = var.template_name
  image_id    = huaweicloud_images_image.image.id
  description = var.template_description
  type        = var.template_type
}

# ELB Load Balancer
resource "huaweicloud_elb_loadbalancer" "elb" {
  count  = var.create_elb ? 1 : 0
  name   = var.elb_name
  type   = var.elb_type
  flavor = var.flavor
}

# ELB Listener
resource "huaweicloud_elb_listener" "listener" {
  name            = "${var.elb_name}-listener"
  protocol        = var.protocol
  protocol_port   = var.port
  loadbalancer_id = huaweicloud_elb_loadbalancer.elb.id
}

# ELB Pool
resource "huaweicloud_elb_pool" "pool" {
  name        = "${var.elb_name}-pool"
  protocol    = var.protocol
  lb_method   = "ROUND_ROBIN"
  listener_id = huaweicloud_elb_listener.listener.id
}

# ELB Member
resource "huaweicloud_elb_member" "member" {
  address       = var.server_address
  protocol_port = var.port
  pool_id       = huaweicloud_elb_pool.pool.id
  subnet_id     = huaweicloud_vpc_subnet.subnet.id
}

# SFS File System
resource "huaweicloud_sfs_file_system" "sfs" {
  count    = var.create_sfs ? 1 : 0
  name     = var.sfs_name
  size     = var.size
  protocol = var.protocol
}

# SFS Access Rule
resource "huaweicloud_sfs_access_rule" "rule" {
  sfs_id       = huaweicloud_sfs_file_system.sfs.id
  access_level = var.access_level
  access_to    = var.access_to
}

# DCS Instance
resource "huaweicloud_dcs_instance" "dcs" {
  count = var.create_dcs ? 1 : 0
  name  = var.dcs_name
}

# DCS Backup
resource "huaweicloud_dcs_backup" "backup" {
  instance_id = huaweicloud_dcs_instance.dcs.id
  name        = var.backup_name
}

# DMS Instance
resource "huaweicloud_dms_instance" "dms" {
  count = var.create_dms ? 1 : 0
  name  = var.dms_name
}

# CCE Cluster
resource "huaweicloud_cce_cluster" "cluster" {
  name         = var.cluster_name
  cluster_type = var.cluster_type
  flavor_id    = "cce.s1.small"
  vpc_id       = huaweicloud_vpc.vpc.id
  subnet_id    = huaweicloud_vpc_subnet.subnet.id
  container_network_type = "overlay_l2"
  authentication_mode    = "rbac"
}

# CCE Node Pool
resource "huaweicloud_cce_node_pool" "node_pool" {
  cluster_id   = huaweicloud_cce_cluster.cluster.id
  name         = var.node_pool_name
  flavor       = var.flavor
  initial_node_count = var.node_count
  availability_zone  = var.availability_zone
  key_pair          = var.key_pair
  root_volume {
    size       = 40
    volumetype = "SAS"
  }
  data_volumes {
    size       = 100
    volumetype = "SAS"
  }
}

# EIP Kaynağı
resource "huaweicloud_vpc_eip" "eip" {
  name         = var.eip_name
  type         = var.eip_type
  bandwidth {
    name       = "${var.eip_name}-bandwidth"
    size       = var.bandwidth
    share_type = "PER"
    charge_mode = var.charge_mode
  }
}

# GaussDB Instance
resource "huaweicloud_gaussdb_mysql_instance" "gaussdb" {
  count = var.create_gaussdb ? 1 : 0
  name  = var.gaussdb_name
  flavor      = var.flavor
  vpc_id      = huaweicloud_vpc.vpc.id
  subnet_id   = huaweicloud_vpc_subnet.subnet.id
  security_group_id = huaweicloud_networking_secgroup.sg.id
  password    = var.db_password
  availability_zone = var.availability_zone

  volume {
    type = "COMMON"
    size = var.storage
  }
}

# WAF Instance
resource "huaweicloud_waf_instance" "waf" {
  count  = var.create_waf ? 1 : 0
  name   = var.waf_name
  domain = var.domain
  server = var.server
}

# WAF Rule
resource "huaweicloud_waf_rule" "waf_rule" {
  count    = var.create_waf_rule ? 1 : 0
  waf_id   = var.waf_id
  type     = var.rule_type
  url      = var.url
  action   = var.action
}

# SSL Certificate
resource "huaweicloud_ssl_certificate" "ssl" {
  count = var.create_ssl ? 1 : 0
  name  = var.ssl_name
  email = var.email
}

# IAM User
resource "huaweicloud_iam_user" "user" {
  count    = var.create_iam_user ? 1 : 0
  name     = var.user_name
  password = var.password
}

# IAM Group
resource "huaweicloud_iam_group" "group" {
  count = var.create_iam_group ? 1 : 0
  name  = var.group_name
}

# IAM Role
resource "huaweicloud_iam_role" "role" {
  count  = var.create_iam_role ? 1 : 0
  name   = var.role_name
  policy = var.policy
}

# MRS Cluster
resource "huaweicloud_mrs_cluster" "mrs" {
  count       = var.create_mrs_cluster ? 1 : 0
  name        = var.cluster_name
  type        = var.cluster_type
  node_count  = var.node_count
  node_flavor = var.node_flavor
}

# MRS Job
resource "huaweicloud_mrs_job" "job" {
  count      = var.create_mrs_job ? 1 : 0
  cluster_id = var.cluster_id
  type       = var.job_type
  name       = var.job_name
  jar_path   = var.jar_path
}

# API Gateway
resource "huaweicloud_apig_api" "api" {
  count        = var.create_api ? 1 : 0
  name         = var.api_name
  group_id     = var.group_id
  path         = var.path
  method       = var.method
  backend_type = var.backend_type
  backend_url  = var.backend_url
}

# API Environment
resource "huaweicloud_apig_environment" "env" {
  count       = var.create_api_env ? 1 : 0
  name         = var.env_name
  description  = var.env_description
}

# Cloud Eye Alarm Rule
resource "huaweicloud_ces_alarmrule" "alarm" {
  count               = var.create_alarm ? 1 : 0
  name                = var.alarm_name
  metric_name         = var.metric_name
  namespace           = var.namespace
  period              = var.period
  statistic           = var.statistic
  threshold           = var.threshold
  comparison_operator = var.comparison_operator
  evaluation_periods  = var.evaluation_periods
  alarm_level         = var.alarm_level
  alarm_action_enabled = true
  alarm_actions {
    type = "notification"
    notification_list = [var.notification_list]
  }
}

# CES Alarm Rule
resource "huaweicloud_ces_alarmrule" "alarm" {
  count               = var.create_alarm ? 1 : 0
  name                = var.alarm_name
  metric_name         = var.metric_name
  namespace           = var.namespace
  period              = var.period
  statistic           = var.statistic
  threshold           = var.threshold
  comparison_operator = var.comparison_operator
  evaluation_periods  = var.evaluation_periods
  alarm_level         = var.alarm_level
  alarm_action_enabled = true
  alarm_actions {
    type = "notification"
    notification_list = [var.notification_list]
  }
}

# KMS Key
resource "huaweicloud_kms_key" "key" {
  count = var.create_kms_key ? 1 : 0
  name  = var.key_name
  type  = var.key_type
}

# CBR Policy
resource "huaweicloud_cbr_policy" "policy" {
  count      = var.create_backup_policy ? 1 : 0
  name       = var.policy_name
  schedule   = var.schedule
  retention  = var.retention
}

# Anti-DDoS
resource "huaweicloud_antiddos" "antiddos" {
  count     = var.create_antiddos ? 1 : 0
  name      = var.antiddos_name
  ip        = var.ip
  bandwidth = var.bandwidth
}

# DWS Cluster
resource "huaweicloud_dws_cluster" "dws" {
  count      = var.create_dws ? 1 : 0
  name       = var.dws_name
  node_type  = var.node_type
}

# CSS Cluster
resource "huaweicloud_css_cluster" "css" {
  count = var.create_css ? 1 : 0
  name  = var.css_name
}

# Çıktılar
output "vpc_list" {
  value = huaweicloud_vpc.vpc
}

output "ecs_list" {
  value = huaweicloud_compute_instance.ecs
}

output "security_group_list" {
  value = huaweicloud_networking_secgroup.sg
}

output "rds_list" {
  value = huaweicloud_rds_instance.rds
}

output "obs_bucket_list" {
  value = huaweicloud_obs_bucket.bucket
}

output "ims_list" {
  value = huaweicloud_images_image.image
}

output "elb_list" {
  value = huaweicloud_elb_loadbalancer.elb
}

output "sfs_list" {
  value = huaweicloud_sfs_file_system.sfs
}

output "dcs_list" {
  value = huaweicloud_dcs_instance.dcs
}

output "dms_list" {
  value = huaweicloud_dms_instance.dms
}

output "cce_cluster_list" {
  value = huaweicloud_cce_cluster.cluster
}

output "waf" {
  value = var.create_waf ? huaweicloud_waf_instance.waf[0] : null
}

output "ssl_certificate" {
  value = var.create_ssl ? huaweicloud_ssl_certificate.ssl[0] : null
}

output "iam_user" {
  value = var.create_iam_user ? huaweicloud_iam_user.user[0] : null
}

output "mrs_cluster" {
  value = var.create_mrs_cluster ? huaweicloud_mrs_cluster.mrs[0] : null
}

output "api_gateway" {
  value = var.create_api ? huaweicloud_apig_api.api[0] : null
}

output "ces_alarm" {
  value = var.create_alarm ? huaweicloud_ces_alarmrule.alarm[0] : null
}

output "kms_key" {
  value = var.create_kms_key ? huaweicloud_kms_key.key[0] : null
}

output "cbr_policy" {
  value = var.create_backup_policy ? huaweicloud_cbr_policy.policy[0] : null
}

output "antiddos" {
  value = var.create_antiddos ? huaweicloud_antiddos.antiddos[0] : null
}

output "dws" {
  value = var.create_dws ? huaweicloud_dws_cluster.dws[0] : null
}

output "css" {
  value = var.create_css ? huaweicloud_css_cluster.css[0] : null
} 