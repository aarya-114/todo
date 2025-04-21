pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                git url: 'https://github.com/aarya-114/todo.git', branch: 'main'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install --user -r requirements.txt'
                sh 'pip3 install --user pytest'
            }
        }

        stage('Build') {
            steps {
                echo '✅ Build complete. App is ready.'
            }
        }

        stage('Run Tests') {
            steps {
                script {
                    // Add the installation directory to PATH
                    sh 'export PATH=$PATH:/Users/aaryapatil/Library/Python/3.9/bin'
                    // Now run the pytest command
                    sh 'pytest test_app.py'
                }
            }
        }
    }

    post {
        success {
            echo '🎉 CI pipeline succeeded!'
        }
        failure {
            echo '❌ CI pipeline failed. Check the logs above.'
        }
    }
}
