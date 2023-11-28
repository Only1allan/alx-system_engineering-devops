#configure nginx server using puppet

exec {'config_nginx':
    provider => shell
    command  => 'sudo apt update -y; sudo apt upgrade -y; sudo apt install nginx -y; sudo service nginx start; \
    sudo chown -R "$USER":"$USER" /var/www/html; echo "Hello world" > /var/www/html/index.nginx-debian.html; \
    sudo sed -i '\#root /var/www/html;#a\\tlocation /redirect_me {\n\t\treturn 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;\n\t}' /etc/nginx/sites-available/default; \
    sudo sed -i '\#root /var/www/html;#a\\terror_page 404 /404.html;\n' /etc/nginx/sites-available/default; \
    echo "Ceci n'est pas une page" > /var/www/html/404.html; sudo service nginx restart,
}