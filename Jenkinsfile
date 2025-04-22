pipeline {
    agent any

    environment {
        IMAGE_NAME = 'flask-library-app'
        CONTAINER_NAME = 'flask-app'
        HOST_PORT = '5018'
        CONTAINER_PORT = '5000'
    }

    stages {

        stage('Checkout Code') {
            steps {
                echo 'Cloning repository...'
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                echo 'Setting up virtual environment and installing dependencies...'
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
                echo 'Building Docker image...'
                sh "docker build -t $IMAGE_NAME ."
            }
        }

        stage('Stop & Remove Old Container') {
            steps {
                echo 'Stopping and removing old container if exists...'
                sh "docker stop $CONTAINER_NAME || true"
                sh "docker rm $CONTAINER_NAME || true"
            }
        }

        stage('Run Container') {
            steps {
                echo 'Running new container...'
                sh """
                    docker run -d \
                    --name $CONTAINER_NAME \
                    -p $HOST_PORT:$CONTAINER_PORT \
                    $IMAGE_NAME
                """
            }
        }
    }

    post {
        always {
            echo 'Pipeline execution completed.'
        }
    }
}
