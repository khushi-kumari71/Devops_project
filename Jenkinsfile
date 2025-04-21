
    pipeline {
    agent any

    stages {
        stage('Install Flask') {
            steps {
                sh 'pip3 install flask'
            }
        }

        stage('Run Flask App') {
            steps {
                sh 'nohup python3 app.py &'
                sleep time: 5, unit: 'SECONDS'
            }
        }

        stage('Health Check') {
            steps {
                sh 'curl http://localhost:5000 || echo "App failed health check"'
            }
        }
    }
}
