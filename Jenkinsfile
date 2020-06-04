pipeline{
        agent any
        stages{

            stage('Enable all scripts to be executable') {
            steps {
                sh 'chmod +x ./script/*'
            }
        }

            stage('get environment ready'){
                steps{
                    sh './script/before_installation.sh'
                    sh './script/installation.sh'
                }
            }

            stage('export database variables'){
                steps{
                    sh 'export DATABASE_URI="mysql+pymysql://${MYSQL_USER}:${MYSQL_PASSWORD}@${MYSQL_HOST}/${MYSQL_DATABASE}"'
                    sh 'export SECRET_KEY=${SECRET_KEY}'
                }
            }



            stage('Run application'){
                steps{
                    sh 'sudo systemctl restart flask.service'
                }
            }
        }    
}