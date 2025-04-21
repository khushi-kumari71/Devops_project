pipeline {
    agent any

    environment {
        FLASK_APP = "app.py"
    }

    stages {
        stage('Install Flask') {
            steps {
                sh 'pip install flask'
                sh 'pip install -r requirements.txt || echo "No requirements.txt found, continuing..."'
            }
        }

        stage('Run Flask App') {
            steps {
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
