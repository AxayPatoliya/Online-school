CREATE SEQUENCE teacher_sno_seq;

CREATE TABLE teacher
(
    sno integer NOT NULL DEFAULT nextval('teacher_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    role character varying(550) COLLATE pg_catalog."default" NOT NULL,
    info character varying(550) COLLATE pg_catalog."default" NOT NULL,
    img_file character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT teacher_pkey PRIMARY KEY (sno)
)