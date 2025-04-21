pipeline {
    agent any

    environment {
        PYTHON_PATH = "/usr/bin:/bin:/usr/sbin:/sbin:/Users/aaryapatil/Library/Python/3.9/bin"
    }

    stages {
        stage('Checkout SCM') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                script {
                    // Install the required dependencies
                    sh 'python3 -m pip install --user -r requirements.txt'
                    sh 'python3 -m pip install --user pytest'
                }
            }
        }

        stage('Build') {
            steps {
                echo "✅ Build complete. App is ready."
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Use python3 -m to call pytest
                    sh 'python3 -m pytest test_app.py'
                }
            }
        }
    }

    post {
        always {
            echo "❌ CI pipeline failed. Check the logs above." 
        }
    }
}
