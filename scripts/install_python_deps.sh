python3 -m venv "$APP_ROOT_PATH"/venv
source "$APP_ROOT_PATH"/venv/bin/activate

len=$#
if [ $len -eq 0 ]; then
  pip install -r "$APP_ROOT_PATH"/requirements/requirements-dev.txt
else
 case "$1" in
   --dev) pip install -r "$APP_ROOT_PATH"/requirements/requirements-dev.txt;;
   --prod) pip install -r "$APP_ROOT_PATH"/requirements/requirements-prod.txt;;
   *) echo "please, use this command with --dev or --prod args only"
      exit 1;; 	
 esac
fi
