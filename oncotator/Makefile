# Definitions
runtime_fullpath = $(realpath runtime)
build_tool = runtime-container.DONE
git_commit ?= $(shell git log --pretty=oneline -n 1 -- ../oncotator | cut -f1 -d " ")
name = jpfeil/oncotator
tag = 1.9--${git_commit}

build:
	docker build -t ${name}:${tag} .
	docker tag ${name}:${tag} ${name}:latest
	touch ${build_tool}

push: build
	# Requires ~/.dockercfg
	docker push ${name}:${tag}
	docker push ${name}:latest

test: build
	python test.py

clean:
	-rm ${build_tool}
