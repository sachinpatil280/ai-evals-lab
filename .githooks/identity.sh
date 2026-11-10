# Shared identity rule for this repo. Sourced by the hooks.
# Every commit and push must belong to the personal account sachinpatil280.
REQUIRED_NAME="sachinpatil280"
REQUIRED_EMAIL="37938690+sachinpatil280@users.noreply.github.com"
REQUIRED_REMOTE="git@github.com-personal:sachinpatil280/ai-evals-lab.git"

die() {
  echo "BLOCKED (identity rule): $1" >&2
  echo "This repo accepts commits and pushes from $REQUIRED_NAME only." >&2
  exit 1
}

email_of() { sed -E 's/.*<([^>]*)>.*/\1/'; }
name_of() { sed -E 's/^(.*) <.*/\1/'; }
