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
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest'
            }
        }
    }

    post {
        success {
            echo '✅ CI pipeline passed successfully!'
        }
        failure {
            echo '❌ CI pipeline failed. Check the logs above.'
        }
    }
}
