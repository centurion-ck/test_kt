terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = "ap-southeast-1"
}

variable "bucket_name" {
  type = string
}

resource "aws_s3_bucket" "bucket" {
  bucket = var.bucket_name

  tags = {
    ManagedBy = "Cloud-Orch"
  }
}