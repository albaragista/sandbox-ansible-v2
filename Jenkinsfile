
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                checkout scm 
                echo 'Building..'
            }
        }
        stage('Test') {
            steps {
                echo 'Testing..'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying....'
                sh 'git pull origin master'
            }
        }
        stage('Add & Commit') {
            steps {
                echo 'Git add.."
            }
        }
    }
}
