pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "sainathmitalakar/python-cli-game"
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/sainathmitalakar/python-game-devops.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                dir('app') {
                    sh 'docker build -t $IMAGE_NAME .'
                }
            }
        }

        stage('Docker Login') {
            steps {
                sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
            }
        }

        stage('Push to Docker Hub') {
            steps {
                sh 'docker push $IMAGE_NAME'
            }
        }

        stage('Clean up') {
            steps {
                sh 'docker logout'
                sh 'docker rmi $IMAGE_NAME || true'
            }
        }
    }

    post {
        success {
            echo '✅ Deployment completed successfully.'
        }
        failure {
            echo '❌ Pipeline failed.'
        }
    }
}
