pipeline {
    agent any

    stages {
        stage('Git') {
            steps {
                git branch: 'main', url: 'https://github.com/rimaesprit/avec-maven.git'
            }
        }
   
        stage('Maven') {
            steps {
                echo 'Hello World'
            }
        }
        stage('Run game') {
            steps {
                echo 'Running Python program'
                sh 'python3 programmejeu.py'
            }
        }
    }
}
