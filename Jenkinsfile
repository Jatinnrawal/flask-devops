pipeline {
    agent any

    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['dev', 'qa', 'prod'],
            description: 'Target environment for this build'
        )
    }

    environment {
        IMAGE_NAME = 'flask-devops-demo'
        VENV = 'venv'
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Setup Virtualenv') {
            steps {
                sh '''
                    python3 -m venv $VENV
                    . $VENV/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Checks') {
            parallel {
                stage('Lint') {
                    steps {
                        echo "Running lint checks..."
                    }
                }
                stage('Unit Tests') {
                    steps {
                        sh '''
                            . $VENV/bin/activate
                            pytest
                        '''
                    }
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }

        stage('Deploy') {
            when {
                expression { return params.ENVIRONMENT == 'prod' }
            }
            steps {
                echo "Deploying ${IMAGE_NAME}:${BUILD_NUMBER} to production..."
            }
        }
    }

    post {
        success {
            echo "Build ${BUILD_NUMBER} succeeded for environment: ${params.ENVIRONMENT}"
        }
        failure {
            echo "Build ${BUILD_NUMBER} failed — check logs above"
        }
        always {
            echo "Pipeline finished"
        }
    }
}
