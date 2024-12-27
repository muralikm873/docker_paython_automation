pipeline {
    agent any
    environment {
        DOCKER_IMAGE = 'docker_paython_automation:latest' // Replace with your preferred image name
    }
    stages {
        stage('Clone Repository') {
            steps {
                git url: 'https://github.com/muralikm873/docker_paython_automation.git', branch: 'main'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    sh 'docker build -t ${DOCKER_IMAGE} .'
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    sh '''
                    docker run --rm \
                    -v $(pwd):/ \
                    -w /app \
                    ${DOCKER_IMAGE} \
                    sh -c "pip install -r requirements.txt && python docker_automation.py"
                    '''
                }
            }
        }
    }
    post {
        success {
            echo 'Job completed successfully.'
        }
        failure {
            echo 'Job failed. Check the logs for details.'
        }
    }
}
