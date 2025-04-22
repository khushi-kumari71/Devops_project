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
                sh '''
                    python3 -m venv venv
                    source venv/bin/activate
                    pip install --break-system-packages -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-library-app .'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'docker run -d --name flask-app -p 5000:5000 flask-library-app'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl --fail http://localhost:5000 || exit 1'
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
