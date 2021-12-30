`docker-compose up` - runs backend on port 8003

# Check that it works
1. Go to [swagger](http://localhost:8003/api/schema/swagger-ui/#/)
2. Fill in fields under create_user POST and click execute
3. Use created user to fill in fields under get_token POST and click execute
4. Copy token from response body
5. Click on Authorize in top right corner
6. Scroll to Token Auth
7. Type "Token", press space then paste in the copied token
8. Execute endpoints they should be authorized now

# Admin
There's also admin credentials are in docker-compose environment DJANGO_SUPERUSER_USERNAME and DJANGO_SUPERUSER_PASSWORD
you can mess around with stuff in db there

# Formatting and import Sorting
`source .venv/Scripts/activate` - Windows (google Linux idc.)
`isort .` - sort all imports, comment them nicely
`black .` - format all files, double quotes etc.