#!/bin/groovy
pipeline {
  agent {
    dockerfile {
      args '--cap-add=SYS_ADMIN --init -v /dev/shm:/dev/shm'
    }
  }
  stages {
    stage('Test') {
      steps {
        ansiColor('xterm') {
          sh "gauge run --tags '!skip'"
        }
      }
      post {
        always {
          publishHTML([
            allowMissing: false,
            alwaysLinkToLastBuild: true,
            keepAll: false,
            reportDir: 'reports/html-report',
            reportFiles: 'index.html',
            reportTitles: 'Gauge Test Results',
            reportName: 'Test Results',
          ])
        }
      }
    }
  }
}
