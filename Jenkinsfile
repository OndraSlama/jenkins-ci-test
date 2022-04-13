pipeline {
    agent any 
    stages {
        stage('Stage 1') {
            steps {
				withCredentials([usernamePassword(credentialsId: 'test_credentials', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
               		sh 'python test_credentials.py --password ${PASS} --username ${USER}'
				}
            }
        }
    }
}