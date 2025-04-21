pipeline {
    agent any

    environment {
        FLASK_APP = "app.py"
    }

    stages {
        stage('Clone Repository') {
            steps {
                git 'https://github.com/khushi-kumari71/Devops_project.git'
            }
        }

        stage('Install Flask') {
            steps {
                sh 'pip install flask'
                sh 'pip install -r requirements.txt || echo "No requirements.txt found, continuing..."'
            }
        }

        stage('Run Flask App') {
            steps {
                // run in background
                sh 'nohup python app.py &'
                sleep time: 10, unit: 'SECONDS'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:5000 || echo "Flask app is not reachable"'
            }
        }
    }
}
