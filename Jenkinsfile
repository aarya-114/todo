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
                    // Run the pytest command to run all the tests
                    bat 'pytest test_app.py'
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
