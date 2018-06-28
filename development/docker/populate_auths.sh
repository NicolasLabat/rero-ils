#! /bin/bash

FLASK_DEBUG=0


# Test if $VIRTUAL_ENV is set
if [ -z "$VIRTUAL_ENV" ]
    then VIRTUAL_ENV="/home/invenio/reroils"
fi

usage="populate_auths.sh [auth_type | all]"

if [ $# -ne 1 ]; then
   echo $usage
   exit 1
fi

case $1 in 
    viaf)                                
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/viaf.json schema http://ils.test.rero.ch/schema/authorities/viaf-v0.0.1.json | invenio records create --pid-minter auth_id
     invenio index reindex --yes-i-know --pid-type auth
     invenio index run -c 4
     ;;

    bnf)                                
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/bnf.json schema http://ils.test.rero.ch/schema/authorities/bnf-v0.0.1.json | invenio records create --pid-minter auth_id
     invenio index reindex --yes-i-know --pid-type auth
     invenio index run -c 4
     ;;

    gnd)                                
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/gnd.json schema http://ils.test.rero.ch/schema/authorities/gnd-v0.0.1.json | invenio records create --pid-minter auth_id
     invenio index reindex --yes-i-know --pid-type auth
     invenio index run -c 4
     ;;

    reroils)                                
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/reroils.json schema http://ils.test.rero.ch/schema/authorities/reroils-v0.0.1.json | invenio records create --pid-minter auth_id
     invenio index reindex --yes-i-know --pid-type auth
     invenio index run -c 4
     ;;

    rero)                                
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/rero.json schema http://ils.test.rero.ch/schema/authorities/rero-v0.0.1.json | invenio records create --pid-minter auth_id
     invenio index reindex --yes-i-know --pid-type auth
     invenio index run -c 4
     ;;
    all)                                
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/rero.json schema http://ils.test.rero.ch/schema/authorities/rero-v0.0.1.json | invenio records create --pid-minter auth_id
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/bnf.json schema http://ils.test.rero.ch/schema/authorities/bnf-v0.0.1.json | invenio records create --pid-minter auth_id
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/gnd.json schema http://ils.test.rero.ch/schema/authorities/gnd-v0.0.1.json | invenio records create --pid-minter auth_id
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/rero.json schema http://ils.test.rero.ch/schema/authorities/rero-v0.0.1.json | invenio records create --pid-minter auth_id
     dojson -i $VIRTUAL_ENV/src/reroils-data/data/reroils.json schema http://ils.test.rero.ch/schema/authorities/reroils-v0.0.1.json | invenio records create --pid-minter auth_id
     invenio index reindex --yes-i-know --pid-type auth
     invenio index run -c 4
  ;;
esac


