resource "aws_vpc" "exam_vpc" {
  cidr_block = "10.0.0.0/16"
  tags = {
    Name = "exam-vpc"
  }
}

resource "aws_subnet" "exam_subnet" {
  vpc_id                  = aws_vpc.exam_vpc.id
  cidr_block              = "10.0.1.0/24"
  map_public_ip_on_launch = true
  tags = {
    Name = "exam-subnet"
  }
}

resource "aws_internet_gateway" "exam_igw" {
  vpc_id = aws_vpc.exam_vpc.id
}

resource "aws_route_table" "exam_rt" {
  vpc_id = aws_vpc.exam_vpc.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.exam_igw.id
  }
}

resource "aws_route_table_association" "exam_rta" {
  subnet_id      = aws_subnet.exam_subnet.id
  route_table_id = aws_route_table.exam_rt.id
}
