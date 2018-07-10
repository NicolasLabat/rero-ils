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

function load_viaf() {
    if [ ! -f $VIRTUAL_ENV/src/reroils-data/data/viaf.json ]; then
        echo "File viaf.json not found!"
    else
        dojson -i $VIRTUAL_ENV/src/reroils-data/data/viaf.json schema http://ils.test.rero.ch/schema/authorities/viaf-v0.0.1.json | invenio records create --pid-minter viaf_id
        invenio index reindex --yes-i-know --pid-type viaf
        invenio index run -c 4
    fi
}


function load_bnf()  {
    if [ ! -f $VIRTUAL_ENV/src/reroils-data/data/bnf.json ]; then
        echo "File bnf.json not found!"
    else
        dojson -i $VIRTUAL_ENV/src/reroils-data/data/bnf.json schema http://ils.test.rero.ch/schema/authorities/bnf-v0.0.1.json | invenio records create --pid-minter bnf_id
        invenio index reindex --yes-i-know --pid-type bnf
        invenio index run -c 4
    fi
}


function load_gnd() {
    if [ ! -f $VIRTUAL_ENV/src/reroils-data/data/gnd.json ]; then
        echo "File gnd.json not found!"
    else
        dojson -i $VIRTUAL_ENV/src/reroils-data/data/gnd.json schema http://ils.test.rero.ch/schema/authorities/gnd-v0.0.1.json | invenio records create --pid-minter gnd_id
        invenio index reindex --yes-i-know --pid-type gnd
        invenio index run -c 4
    fi
}


function load_rero() {
    if [ ! -f $VIRTUAL_ENV/src/reroils-data/data/rero.json ]; then
        echo "File rero.json not found!"
    else
        dojson -i $VIRTUAL_ENV/src/reroils-data/data/rero.json schema http://ils.test.rero.ch/schema/authorities/rero-v0.0.1.json | invenio records create --pid-minter rero_id
        invenio index reindex --yes-i-know --pid-type rero
        invenio index run -c 4
    fi
}

function load_reroils() {
    if [ ! -f $VIRTUAL_ENV/src/reroils-data/data/reroils.json ]; then
        echo "File reroils.json not found!"
    else
        dojson -i $VIRTUAL_ENV/src/reroils-data/data/reroils.json schema http://ils.test.rero.ch/schema/authorities/reroils-v0.0.1.json | invenio records create --pid-minter mef_id
        invenio index reindex --yes-i-know --pid-type mef
        invenio index run -c 4
    fi
}

case $1 in 
    viaf)                                
        load_viaf
    ;;
    bnf)                                
        load_bnf
    ;;
    gnd)                                
        load_gnd
    ;;
    rero)                                
        load_rero
    ;;
    reroils)                                
        load_reroils
    ;;
    all)                                
        load_viaf
        load_bnf
        load_gnd
        load_rero
        load_reroils
    ;;
    *)
        echo "Invalid input!"
    ;;
esac