# Security Outputs
output "security_group" {
  description = "Created security group details"
  value       = var.create_security_group ? huaweicloud_networking_secgroup.sg[0] : null
}

output "waf" {
  description = "Created WAF instance details"
  value       = var.create_waf ? huaweicloud_waf_instance.waf[0] : null
}

output "ssl_certificate" {
  description = "Created SSL certificate details"
  value       = var.create_ssl ? huaweicloud_ssl_certificate.ssl[0] : null
}

# IAM Outputs
output "iam_user" {
  description = "Created IAM user details"
  value       = var.create_iam_user ? huaweicloud_iam_user.user[0] : null
}

output "iam_group" {
  description = "Created IAM group details"
  value       = var.create_iam_group ? huaweicloud_iam_group.group[0] : null
}

output "iam_role" {
  description = "Created IAM role details"
  value       = var.create_iam_role ? huaweicloud_iam_role.role[0] : null
}

# Compute Outputs
output "mrs_cluster" {
  description = "Created MRS cluster details"
  value       = var.create_mrs_cluster ? huaweicloud_mrs_cluster.mrs[0] : null
}

output "mrs_job" {
  description = "Created MRS job details"
  value       = var.create_mrs_job ? huaweicloud_mrs_job.job[0] : null
}

# API Gateway Outputs
output "api_gateway" {
  description = "Created API Gateway details"
  value       = var.create_api ? huaweicloud_apig_api.api[0] : null
}

output "api_environment" {
  description = "Created API environment details"
  value       = var.create_api_env ? huaweicloud_apig_environment.env[0] : null
}

# Monitoring Outputs
output "ces_alarm" {
  description = "Created CES alarm rule details"
  value       = var.create_alarm ? huaweicloud_ces_alarmrule.alarm[0] : null
}

# Security Service Outputs
output "kms_key" {
  description = "Created KMS key details"
  value       = var.create_kms_key ? huaweicloud_kms_key.key[0] : null
}

output "cbr_policy" {
  description = "Created CBR policy details"
  value       = var.create_backup_policy ? huaweicloud_cbr_policy.policy[0] : null
}

output "antiddos" {
  description = "Created Anti-DDoS details"
  value       = var.create_antiddos ? huaweicloud_antiddos.antiddos[0] : null
}

# Network Outputs
output "elb" {
  description = "Created ELB details"
  value       = var.create_elb ? huaweicloud_elb_loadbalancer.elb[0] : null
}

# Storage Outputs
output "obs_bucket" {
  description = "Created OBS bucket details"
  value       = var.create_obs ? huaweicloud_obs_bucket.bucket[0] : null
}

output "sfs" {
  description = "Created SFS details"
  value       = var.create_sfs ? huaweicloud_sfs_file_system.sfs[0] : null
}

# Database Outputs
output "rds" {
  description = "Created RDS instance details"
  value       = var.create_rds ? huaweicloud_rds_instance.rds[0] : null
}

output "dcs" {
  description = "Created DCS instance details"
  value       = var.create_dcs ? huaweicloud_dcs_instance.dcs[0] : null
}

output "dms" {
  description = "Created DMS instance details"
  value       = var.create_dms ? huaweicloud_dms_instance.dms[0] : null
}

output "gaussdb" {
  description = "Created GaussDB instance details"
  value       = var.create_gaussdb ? huaweicloud_gaussdb_instance.gaussdb[0] : null
}

output "dws" {
  description = "Created DWS cluster details"
  value       = var.create_dws ? huaweicloud_dws_cluster.dws[0] : null
}

output "css" {
  description = "Created CSS cluster details"
  value       = var.create_css ? huaweicloud_css_cluster.css[0] : null
} 