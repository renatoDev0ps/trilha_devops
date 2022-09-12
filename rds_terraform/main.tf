provider "aws" {
  region = "us-east-1"
}

resource "aws_db_instance" "dioLiveDB" {
  allocated_storage = 20
  identifier = "diolivedb"
  storage_type = "gp2"
  engine = "mysql"
  engine_version = "8.0.27"
  instance_class = "db.t2.micro"
  db_name = "dioLiveDB"
  username = "admin"
  password = "admin1234"
  publicly_accessible = true
  skip_final_snapshot = true

  tags = {
    Name = "dioLiveDB"
  }
}