resource "aws_security_group" "exam_sg" {
  name   = "exam-sg"
  vpc_id = aws_vpc.exam_vpc.id

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}

resource "aws_instance" "exam_ec2" {
  ami                    = "ami-0c02fb55956c7d316" # Amazon Linux 2 (us-east-1)
  instance_type          = "t3.micro"
    key_name = "terraform-key" 
  subnet_id              = aws_subnet.exam_subnet.id
  vpc_security_group_ids = [aws_security_group.exam_sg.id]

  tags = {
    Name = "exam-ec2"
  }
}
