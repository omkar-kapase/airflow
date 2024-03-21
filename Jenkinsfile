pipeline {
    agent any

    environment {
        // Define environment variables
        GITHUB_REPO_URL = 'https://github.com/omkar-kapase/airflow.git'
        DOCKERFILE_PATH = 'Dockerfile'
        ACR_NAME = 'airflowim.azurecr.io'
        AZURE_CREDENTIALS_ID = 'acr-mnp'
        HELM_CHART_PATH = 'airflow1'
        HELM_RELEASE_NAME = 'airflow1'
        K8S_NAMESPACE = 'default'
        K8S_CREDENTIALS_ID = 'k8s' // Update with your actual Kubernetes credentials ID
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo "Checking out code from ${GITHUB_REPO_URL}"
                    git branch: 'main', credentialsId: 'github', url: GITHUB_REPO_URL
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo "Building Docker image from ${DOCKERFILE_PATH}"
                    sh "docker build -t ${ACR_NAME}/airflow1:latest -f ${DOCKERFILE_PATH} ."
                }
            }
        }

        stage('Push to ACR') {
            steps {
                script {
                    echo "Pushing Docker image to ${ACR_NAME}.airflowim.azurecr.io"
                    withCredentials([azureServicePrincipal(credentialsId: AZURE_CREDENTIALS_ID)]) {
                        sh "az login --service-principal --username \${AZURE_CLIENT_ID} --password \${AZURE_CLIENT_SECRET} --tenant \${AZURE_TENANT_ID}"
                        sh "az acr login --name ${ACR_NAME}"
                        sh "docker tag ${ACR_NAME}/airflow1:latest ${ACR_NAME}/airflow1:latest"
                        sh "docker push ${ACR_NAME}/airflow1:latest"
                        sh "az logout"
                    }
                }
            }
        }

        // stage('Deploy') {
        //     steps {
        //         script {
        //             echo "Deploying Docker image using docker run"
        //             sh "docker run -p 8081:8080 -v /usr/local/airflow/dags:/opt/airflow/dags -d ${ACR_NAME}/airflow1:"
        //         }
        //     }
        // }
    }

    post {
        success {
            cleanWs()
            sh "docker rmi -f ${ACR_NAME}/airflow1:latest"
        }
    }
}
