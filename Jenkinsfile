
    pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/khushi-kumari71/Devops_project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt || true'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-library-app .'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'docker run -d -p 5000:5000 --name flask-app flask-library-app'
            }
        }

        stage('Health Check') {
            steps {
                sh 'sleep 5'
                sh 'curl -f http://localhost:5000 || echo "Health check failed"'
            }
        }
    }

    post {
        always {
            echo 'Cleaning up...'
            sh 'docker stop flask-app || true'
            sh 'docker rm flask-app || true'
        }
    }
}
