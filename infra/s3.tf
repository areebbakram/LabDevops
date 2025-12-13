resource "random_id" "bucket_id" {
  byte_length = 4
}

resource "aws_s3_bucket" "exam_bucket" {
  bucket = "exam-devops-${random_id.bucket_id.hex}"
}
