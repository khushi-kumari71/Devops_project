pipeline {
    agent any  // Runs the pipeline on any available agent
    
    environment {
        // Set up any environment variables you may need
        MY_ENV_VAR = "value"
    }

    stages {
        stage('Checkout') {
            steps {
                // Pulls the code from the repository
                git 'https://github.com/khushi-kumari71/Devops_project.git'
            }
        }
        
        stage('Build') {
            steps {
                // Compile/build your project (example for a Maven project)
                sh 'mvn clean install'
            }
        }
        
        stage('Test') {
            steps {
                // Run unit tests (example for a Maven project)
                sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                // Example: Deploy your application to a server
                echo 'Deploying the application'
                // Add deployment commands here (e.g., SCP, Docker, etc.)
            }
        }
    }

    post {
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
