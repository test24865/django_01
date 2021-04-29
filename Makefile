run:
	 cd blog && python manage.py runserver


make-migrate:
	python blog/manage.py makemigrations


migrate:
	python blog/manage.py migrate


lint:
	flake8 ./blog

check:
	python blog/manage.py check

check-migrate:
	python blog/manage.py makemigrations --check --dry-run

shell_plus:
	python blog/manage.py shell_plus --print-sql

#celery:
	# celery -A blog worker -l info
#
#celery_autoscale:
#		celery -A blog worker --autoscale=4,2 -l info


