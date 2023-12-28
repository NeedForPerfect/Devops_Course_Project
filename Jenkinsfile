pipeline {
 agent any
 environment {
    MY_NAME = 'Volodymyr'
 }
 stages {
  stage("Create file") {
   steps {
    script {
      sh 'echo ${MY_NAME} >> text.txt'
      sh 'pwd'
    }
   }
 }
  
  stage('Show file content') {
    steps {
        sh 'cat text.txt'
    }
  }
  
 }
}

