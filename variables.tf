# Provider variables
variable "region" {
  description = "Huawei Cloud region"
  type        = string
}

variable "access_key" {
  description = "Huawei Cloud access key"
  type        = string
  sensitive   = true
}

variable "secret_key" {
  description = "Huawei Cloud secret key"
  type        = string
  sensitive   = true
}

# Security Group variables
variable "create_security_group" {
  description = "Whether to create security group"
  type        = bool
  default     = false
}

variable "security_group_name" {
  description = "Name of the security group"
  type        = string
}

variable "description" {
  description = "Description of the security group"
  type        = string
}

variable "vpc_id" {
  description = "VPC ID"
  type        = string
}

variable "create_security_group_rule" {
  description = "Whether to create security group rule"
  type        = bool
  default     = false
}

variable "security_group_id" {
  description = "Security group ID"
  type        = string
}

variable "direction" {
  description = "Direction of the security group rule"
  type        = string
}

variable "protocol" {
  description = "Protocol of the security group rule"
  type        = string
}

variable "port_range_min" {
  description = "Minimum port range"
  type        = number
}

variable "port_range_max" {
  description = "Maximum port range"
  type        = number
}

variable "remote_ip_prefix" {
  description = "Remote IP prefix"
  type        = string
}

# WAF variables
variable "create_waf" {
  description = "Whether to create WAF"
  type        = bool
  default     = false
}

variable "waf_name" {
  description = "Name of the WAF"
  type        = string
}

variable "domain" {
  description = "Domain name"
  type        = string
}

variable "server" {
  description = "Server IP"
  type        = string
}

variable "create_waf_rule" {
  description = "Whether to create WAF rule"
  type        = bool
  default     = false
}

variable "waf_id" {
  description = "WAF ID"
  type        = string
}

variable "rule_type" {
  description = "Type of the WAF rule"
  type        = string
}

variable "url" {
  description = "URL for WAF rule"
  type        = string
}

variable "action" {
  description = "Action for WAF rule"
  type        = string
}

# SSL Certificate variables
variable "create_ssl" {
  description = "Whether to create SSL certificate"
  type        = bool
  default     = false
}

variable "ssl_name" {
  description = "Name of the SSL certificate"
  type        = string
}

variable "email" {
  description = "Email address"
  type        = string
}

# IAM variables
variable "create_iam_user" {
  description = "Whether to create IAM user"
  type        = bool
  default     = false
}

variable "user_name" {
  description = "Name of the IAM user"
  type        = string
}

variable "password" {
  description = "Password for IAM user"
  type        = string
  sensitive   = true
}

variable "create_iam_group" {
  description = "Whether to create IAM group"
  type        = bool
  default     = false
}

variable "group_name" {
  description = "Name of the IAM group"
  type        = string
}

variable "create_iam_role" {
  description = "Whether to create IAM role"
  type        = bool
  default     = false
}

variable "role_name" {
  description = "Name of the IAM role"
  type        = string
}

variable "policy" {
  description = "IAM policy"
  type        = string
}

# MRS variables
variable "create_mrs_cluster" {
  description = "Whether to create MRS cluster"
  type        = bool
  default     = false
}

variable "cluster_name" {
  description = "Name of the MRS cluster"
  type        = string
}

variable "cluster_type" {
  description = "Type of the MRS cluster"
  type        = string
}

variable "node_count" {
  description = "Number of nodes"
  type        = number
}

variable "node_flavor" {
  description = "Flavor of the nodes"
  type        = string
}

variable "create_mrs_job" {
  description = "Whether to create MRS job"
  type        = bool
  default     = false
}

variable "cluster_id" {
  description = "Cluster ID"
  type        = string
}

variable "job_type" {
  description = "Type of the MRS job"
  type        = string
}

variable "job_name" {
  description = "Name of the MRS job"
  type        = string
}

variable "jar_path" {
  description = "Path to the JAR file"
  type        = string
}

# API Gateway variables
variable "create_api" {
  description = "Whether to create API"
  type        = bool
  default     = false
}

variable "api_name" {
  description = "Name of the API"
  type        = string
}

variable "group_id" {
  description = "API group ID"
  type        = string
}

variable "path" {
  description = "API path"
  type        = string
}

variable "method" {
  description = "HTTP method"
  type        = string
}

variable "backend_type" {
  description = "Type of the backend"
  type        = string
}

variable "backend_url" {
  description = "Backend URL"
  type        = string
}

variable "create_api_env" {
  description = "Whether to create API environment"
  type        = bool
  default     = false
}

variable "env_name" {
  description = "Name of the API environment"
  type        = string
}

variable "env_description" {
  description = "Description of the API environment"
  type        = string
}

# CES variables
variable "create_alarm" {
  description = "Whether to create alarm rule"
  type        = bool
  default     = false
}

variable "alarm_name" {
  description = "Name of the alarm rule"
  type        = string
}

variable "metric_name" {
  description = "Name of the metric"
  type        = string
}

variable "threshold" {
  description = "Threshold value"
  type        = number
}

variable "comparison_operator" {
  description = "Comparison operator"
  type        = string
}

variable "period" {
  description = "Period in seconds"
  type        = number
}

# KMS variables
variable "create_kms_key" {
  description = "Whether to create KMS key"
  type        = bool
  default     = false
}

variable "key_name" {
  description = "Name of the KMS key"
  type        = string
}

variable "key_type" {
  description = "Type of the KMS key"
  type        = string
}

# CBR variables
variable "create_backup_policy" {
  description = "Whether to create backup policy"
  type        = bool
  default     = false
}

variable "policy_name" {
  description = "Name of the backup policy"
  type        = string
}

variable "schedule" {
  description = "Backup schedule"
  type        = string
}

variable "retention" {
  description = "Retention period in days"
  type        = number
}

# Anti-DDoS variables
variable "create_antiddos" {
  description = "Whether to create Anti-DDoS"
  type        = bool
  default     = false
}

variable "antiddos_name" {
  description = "Name of the Anti-DDoS"
  type        = string
}

variable "ip" {
  description = "IP address"
  type        = string
}

variable "bandwidth" {
  description = "Bandwidth in Mbps"
  type        = number
}

# ELB variables
variable "create_elb" {
  description = "Whether to create ELB"
  type        = bool
  default     = false
}

variable "elb_name" {
  description = "Name of the ELB"
  type        = string
}

variable "elb_type" {
  description = "Type of the ELB"
  type        = string
}

variable "flavor" {
  description = "Flavor of the resource"
  type        = string
}

# OBS variables
variable "create_obs" {
  description = "Whether to create OBS bucket"
  type        = bool
  default     = false
}

variable "bucket_name" {
  description = "Name of the OBS bucket"
  type        = string
}

variable "storage_class" {
  description = "Storage class of the OBS bucket"
  type        = string
}

variable "versioning" {
  description = "Whether to enable versioning"
  type        = bool
  default     = false
}

# SFS variables
variable "create_sfs" {
  description = "Whether to create SFS"
  type        = bool
  default     = false
}

variable "sfs_name" {
  description = "Name of the SFS"
  type        = string
}

variable "size" {
  description = "Size of the SFS"
  type        = number
}

variable "protocol" {
  description = "Protocol of the SFS"
  type        = string
}

# RDS variables
variable "create_rds" {
  description = "Whether to create RDS instance"
  type        = bool
  default     = false
}

variable "rds_name" {
  description = "Name of the RDS instance"
  type        = string
}

variable "engine" {
  description = "Database engine"
  type        = string
}

variable "version" {
  description = "Version of the resource"
  type        = string
}

# DCS variables
variable "create_dcs" {
  description = "Whether to create DCS instance"
  type        = bool
  default     = false
}

variable "dcs_name" {
  description = "Name of the DCS instance"
  type        = string
}

# DMS variables
variable "create_dms" {
  description = "Whether to create DMS instance"
  type        = bool
  default     = false
}

variable "dms_name" {
  description = "Name of the DMS instance"
  type        = string
}

# GaussDB variables
variable "create_gaussdb" {
  description = "Whether to create GaussDB instance"
  type        = bool
  default     = false
}

variable "gaussdb_name" {
  description = "Name of the GaussDB instance"
  type        = string
}

# DWS variables
variable "create_dws" {
  description = "Whether to create DWS cluster"
  type        = bool
  default     = false
}

variable "dws_name" {
  description = "Name of the DWS cluster"
  type        = string
}

variable "node_type" {
  description = "Type of the node"
  type        = string
}

# CSS variables
variable "create_css" {
  description = "Whether to create CSS cluster"
  type        = bool
  default     = false
}

variable "css_name" {
  description = "Name of the CSS cluster"
  type        = string
}

variable "vpc_name" {
  description = "VPC adı"
  type        = string
}

variable "vpc_cidr" {
  description = "VPC CIDR bloğu"
  type        = string
}

variable "ecs_name" {
  description = "ECS instance adı"
  type        = string
}

variable "availability_zone" {
  description = "Kullanılabilirlik bölgesi"
  type        = string
  default     = "eu-west-101a"
}

variable "sg_name" {
  description = "Güvenlik grubu adı"
  type        = string
}

variable "sg_description" {
  description = "Güvenlik grubu açıklaması"
  type        = string
}

# RDS Değişkenleri
variable "db_type" {
  description = "Veritabanı tipi"
  type        = string
}

variable "db_version" {
  description = "Veritabanı versiyonu"
  type        = string
}

variable "db_password" {
  description = "Veritabanı şifresi"
  type        = string
  sensitive   = true
}

variable "storage" {
  description = "Depolama boyutu (GB)"
  type        = number
}

variable "backup_name" {
  description = "RDS yedekleme adı"
  type        = string
}

# OBS Değişkenleri
variable "object_key" {
  description = "OBS object anahtarı"
  type        = string
}

variable "file_path" {
  description = "Yüklenecek dosya yolu"
  type        = string
}

# IMS Değişkenleri
variable "image_name" {
  description = "Image adı"
  type        = string
}

variable "ecs_id" {
  description = "Kaynak ECS ID"
  type        = string
}

variable "description" {
  description = "Image açıklaması"
  type        = string
}

variable "project_id" {
  description = "Paylaşılacak proje ID"
  type        = string
}

variable "image_type" {
  description = "Image tipi (ECS, BMS, Ironic)"
  type        = string
}

variable "min_disk" {
  description = "Minimum disk boyutu (GB)"
  type        = number
}

variable "min_ram" {
  description = "Minimum RAM (MB)"
  type        = number
}

variable "tags" {
  description = "Image etiketleri"
  type        = map(string)
  default     = {}
}

variable "share_type" {
  description = "Paylaşım tipi (Proje, Domain)"
  type        = string
}

variable "share_duration" {
  description = "Paylaşım süresi (saat)"
  type        = number
}

variable "source_image_id" {
  description = "Kaynak image ID"
  type        = string
}

variable "target_region" {
  description = "Hedef bölge"
  type        = string
}

variable "target_image_name" {
  description = "Hedef image adı"
  type        = string
}

variable "copy_type" {
  description = "Kopyalama tipi (Tam Kopya, Hızlı Kopya)"
  type        = string
}

variable "version_name" {
  description = "Versiyon adı"
  type        = string
}

variable "version_description" {
  description = "Versiyon açıklaması"
  type        = string
}

variable "is_protected" {
  description = "Korumalı versiyon"
  type        = bool
  default     = false
}

variable "template_name" {
  description = "Şablon adı"
  type        = string
}

variable "template_description" {
  description = "Şablon açıklaması"
  type        = string
}

variable "template_type" {
  description = "Şablon tipi (Sistem, Özel)"
  type        = string
}

# ELB Değişkenleri
variable "bandwidth" {
  description = "Bant genişliği (Mbps)"
  type        = number
}

variable "port" {
  description = "Port numarası"
  type        = number
}

variable "server_address" {
  description = "Sunucu adresi"
  type        = string
}

# SFS Değişkenleri
variable "access_level" {
  description = "Erişim seviyesi"
  type        = string
}

variable "access_to" {
  description = "Erişim IP/CIDR"
  type        = string
}

# DCS Değişkenleri
variable "engine_version" {
  description = "Motor versiyonu"
  type        = string
}

variable "capacity" {
  description = "Kapasite (GB)"
  type        = number
}

# DMS Değişkenleri
variable "storage_space" {
  description = "Depolama alanı (GB)"
  type        = number
}

variable "topic_name" {
  description = "Topic adı"
  type        = string
}

# CCE Değişkenleri
variable "cluster_version" {
  description = "Kubernetes versiyonu"
  type        = string
}

variable "node_pool_name" {
  description = "Node pool adı"
  type        = string
}

# EIP Değişkenleri
variable "eip_name" {
  description = "EIP adı"
  type        = string
}

variable "eip_type" {
  description = "EIP tipi"
  type        = string
}

variable "charge_mode" {
  description = "Ödeme modu"
  type        = string
}

# GaussDB Değişkenleri
variable "instance_name" {
  description = "Instance adı"
  type        = string
}

# WAF Değişkenleri
variable "policy_type" {
  description = "Politika tipi"
  type        = string
}

variable "protection_mode" {
  description = "Koruma modu"
  type        = string
}

variable "rule_name" {
  description = "Kural adı"
  type        = string
}

variable "rule_action" {
  description = "Kural aksiyonu"
  type        = string
}

variable "rule_priority" {
  description = "Kural önceliği"
  type        = number
}

variable "rule_field" {
  description = "Kural alanı"
  type        = string
}

variable "rule_logic" {
  description = "Kural mantığı"
  type        = string
}

variable "rule_content" {
  description = "Kural içeriği"
  type        = string
}

# ModelArts Değişkenleri
variable "workspace_name" {
  description = "Workspace adı"
  type        = string
}

variable "workspace_description" {
  description = "Workspace açıklaması"
  type        = string
}

variable "enterprise_project_id" {
  description = "Enterprise proje ID"
  type        = string
}

# MRS Değişkenleri
variable "master_flavor" {
  description = "Master node tipi"
  type        = string
}

variable "master_count" {
  description = "Master node sayısı"
  type        = number
}

variable "core_flavor" {
  description = "Core node tipi"
  type        = string
}

variable "core_count" {
  description = "Core node sayısı"
  type        = number
}

# API Gateway Değişkenleri
variable "api_group_id" {
  description = "API grup ID"
  type        = string
}

variable "api_type" {
  description = "API tipi"
  type        = string
}

variable "request_protocol" {
  description = "İstek protokolü"
  type        = string
}

variable "request_method" {
  description = "İstek metodu"
  type        = string
}

variable "request_path" {
  description = "İstek yolu"
  type        = string
}

# Cloud Eye Değişkenleri
variable "alarm_level" {
  description = "Alarm seviyesi"
  type        = string
}

variable "notification_list" {
  description = "Bildirim listesi"
  type        = list(string)
} 