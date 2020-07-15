CREATE SEQUENCE scroll_sno_seq;

CREATE TABLE scroll
(
    sno integer NOT NULL DEFAULT nextval('scroll_sno_seq'::regclass),
    scroll_notice text COLLATE pg_catalog."default" NOT NULL,
    date date DEFAULT CURRENT_DATE,
    CONSTRAINT scroll_pkey PRIMARY KEY (sno)
)