pipeline {
  environment {
    registry = "jaydeegb23/web-calculator"
    registryCredential = "docker_auth"
    dockerImage = ''
  }

  agent any

  options {
    skipStagesAfterUnstable()
  }

  stages {
    stage('Cloning our Git') {
    		steps {
            git branch: 'main',
            url: 'https://github.com/jaydeegbobeh/eng88_flaskcalculator.git'
    		}
    }

    stage('Build') {
      agent {
          docker {
              image 'python:3'
          }
      }
      steps {
          sh './build.sh'
          stash(name: 'compiled-results', includes: 'calculator/*.py*')
      }
    }

    stage('Test') {
    	agent {
    			docker {
    					image 'qnib/pytest'
    			}
    	}
    	steps {
    			sh 'py.test --junit-xml test-reports/results.xml calculator/calc_test.py'
    	}
    	post {
    			always {
    					junit 'test-reports/results.xml'
    			}
    	}
    }

    stage('Build-Image') {
    	steps{
    			script {
    			dockerImage = docker.build registry + ":$BUILD_NUMBER"
    			}
    	}
    }

    stage('Deploy Image') {
    	steps{
    			script {
    					docker.withRegistry( '', registryCredential ) {
    							dockerImage.push()
    					}
    			}
    	}
    }

    stage('Remove Unused docker image') {
    	steps{
    			sh "docker rmi $registry:$BUILD_NUMBER"
    	}
    }
  }
}
