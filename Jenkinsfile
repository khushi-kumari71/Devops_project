
pipeline {
    agent any

    environment {
        IMAGE_NAME = "flask-library-app"
        CONTAINER_NAME = "flask-app"
        HOST_PORT = "5018"
        CONTAINER_PORT = "5000"
    }

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
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t $IMAGE_NAME .'
            }
        }

        stage('Stop and Remove Old Container') {
            steps {
                sh 'docker stop $CONTAINER_NAME || true'
                sh 'docker rm $CONTAINER_NAME || true'
            }
        }

        stage('Run New Container') {
            steps {
                sh '''
                    docker run -d \
                    --name $CONTAINER_NAME \
                    -p $HOST_PORT:$CONTAINER_PORT \
                    $IMAGE_NAME
                '''
            }
        }
    }

    post {
        always {
            echo '✅ Pipeline finished.'
        }
    }
}
