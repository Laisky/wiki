# db . -t ppcelery/wiki:20230421
FROM python:3.10.4-bullseye AS linter

WORKDIR /app
USER root:root

RUN pip install kipp
ADD . .
RUN make lint
RUN python ./_scripts/link_to_term.py --dir=./content --write
RUN cd /app/themes && git clone https://github.com/Laisky/hugo-book.git

FROM golang:1.21.5-bullseye AS gobuild

RUN go install -tags extended github.com/gohugoio/hugo@latest

# COPY --from=linter /app /app
# WORKDIR /app
# RUN /go/bin/hugo --minify --cleanDestinationDir --destination=/app/public --baseURL=https://wiki.laisky.com

FROM debian:bullseye AS final

COPY --from=linter /app /app
COPY --from=gobuild /go/bin/hugo /go/bin/hugo
WORKDIR /app


ENTRYPOINT [ "/go/bin/hugo" , "server"]
CMD [ "--minify", "--cleanDestinationDir", "--destination=/app/public", "--baseURL=https://wiki.laisky.com", "--bind=0.0.0.0", "--appendPort=false"]
