
    pipeline {
    agent any

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t flask-library-app .'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'docker run -d -p 5000:5000 flask-library-app'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl --fail http://localhost:5000 || exit 1'
            }
        }
    }
}
