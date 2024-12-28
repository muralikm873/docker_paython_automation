pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                // Clone the GitHub repository containing the Python script
                git branch: 'main', url: 'https://github.com/muralikm873/docker_paython_automation.git'
            }
        }
        stage('Setup Virtual Environment') {
            steps {
                // Create and activate a Python virtual environment
                sh '''
                python3 -m venv venv
                . venv/bin/activate
                pip install --upgrade pip
                pip install docker psutil
                '''
            }
        }

        stage('Run Python Script') {
            steps {
                // Run the Python script using the virtual environment
                sh '''
                . venv/bin/activate
                python docker_automation.py
                '''
            }
        }
    }

    post {
        always {
            // Cleanup workspace
            cleanWs()
        }
        failure {
            // Notify on failure (optional)
            echo 'Build failed! Check the logs for details.'
        }
        success {
            // Notify on success (optional)
            echo 'Build succeeded!'
        }
    }
}
