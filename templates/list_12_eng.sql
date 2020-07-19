
CREATE SEQUENCE l12_eng_sno_seq;

CREATE TABLE l12_eng
(
    sno integer NOT NULL DEFAULT nextval('l12_eng_sno_seq'::regclass),
    name text COLLATE pg_catalog."default" NOT NULL,
    decr text COLLATE pg_catalog."default" NOT NULL,
    pdf_decr1 text COLLATE pg_catalog."default" NOT NULL,
    pdf_file1 character varying(50) COLLATE pg_catalog."default" NOT NULL,
    pdf_decr2 text COLLATE pg_catalog."default" NOT NULL,
    pdf_file2 character varying(50) COLLATE pg_catalog."default" NOT NULL,
    pdf_decr3 text COLLATE pg_catalog."default" NOT NULL,
    pdf_file3 character varying(50) COLLATE pg_catalog."default" NOT NULL,
    video_decr1 text COLLATE pg_catalog."default" NOT NULL,
    video_file1 character varying(50) COLLATE pg_catalog."default" NOT NULL,
    video_decr2 text COLLATE pg_catalog."default" NOT NULL,
    video_file2 character varying(50) COLLATE pg_catalog."default" NOT NULL,
    video_decr3 text COLLATE pg_catalog."default" NOT NULL,
    video_file3 character varying(50) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT l12_eng_pkey PRIMARY KEY (sno)
)
