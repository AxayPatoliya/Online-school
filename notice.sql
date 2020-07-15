CREATE SEQUENCE notice_sno_seq;

CREATE TABLE notice
(
    sno integer NOT NULL DEFAULT nextval('notice_sno_seq'::regclass),
    category text COLLATE pg_catalog."default" NOT NULL,
    title text COLLATE pg_catalog."default" NOT NULL,
    content text COLLATE pg_catalog."default" NOT NULL,
    img_file character varying(50) COLLATE pg_catalog."default" NOT NULL,
    date date DEFAULT CURRENT_DATE,
    slug character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT notice_pkey PRIMARY KEY (sno)
)

