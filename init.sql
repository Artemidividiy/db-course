DROP TABLE IF EXISTS public.types CASCADE;

CREATE TABLE  public.types
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT types_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;  

ALTER TABLE IF EXISTS public.types
    OWNER to postgres;

-- Table: public.countries
DROP TABLE IF EXISTS public.countries CASCADE;

CREATE TABLE public.countries
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT countries_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.countries
    OWNER to postgres;

-- Table: public.emploees

DROP TABLE IF EXISTS public.emploees CASCADE;

CREATE TABLE  public.emploees
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    "position" integer NOT NULL,
    "birth year" date NOT NULL,
    priority integer NOT NULL,
    CONSTRAINT emploee_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.emploees
    OWNER to postgres;

-- Table: public.emploees_stocks

DROP TABLE IF EXISTS public.emploees_stocks CASCADE;

CREATE TABLE  public.emploees_stocks
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    stock_id integer NOT NULL,
    emploee_id integer NOT NULL,
    CONSTRAINT emploees_stocks_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.emploees_stocks
    OWNER to postgres;

-- Table: public.items

DROP TABLE IF EXISTS public.items CASCADE;

CREATE TABLE  public.items
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    type integer NOT NULL,
    stock integer NOT NULL,
    name character varying COLLATE pg_catalog."default" NOT NULL,
    arrival_time time without time zone NOT NULL,
    arrival_date date NOT NULL,
    "point of departure" integer NOT NULL,
    CONSTRAINT items_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.items
    OWNER to postgres;
-- Table: public.places

DROP TABLE IF EXISTS public.places CASCADE;

CREATE TABLE IF NOT EXISTS public.places
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "Name" character varying COLLATE pg_catalog."default" NOT NULL,
    "Organization" integer,
    longitude double precision NOT NULL,
    latitude double precision NOT NULL,
    "Country" integer NOT NULL,
    CONSTRAINT "Places_pkey" PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.places
    OWNER to postgres;


-- Table: public.positions

DROP TABLE IF EXISTS public.positions CASCADE;

CREATE TABLE  public.positions
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT positions_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.positions
    OWNER to postgres;

-- Table: public.priorities

DROP TABLE IF EXISTS public.priorities CASCADE;

CREATE TABLE  public.priorities
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    "number" integer NOT NULL,
    CONSTRAINT priority_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.priorities
    OWNER to postgres;

-- Table: public.stocks

DROP TABLE IF EXISTS public.stocks CASCADE;

CREATE TABLE  public.stocks
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying COLLATE pg_catalog."default",
    longitude double precision NOT NULL,
    latitude double precision NOT NULL,
    country integer NOT NULL,
    CONSTRAINT stocks_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stocks
    OWNER to postgres;

-- Table: public.organizations

DROP TABLE IF EXISTS public.organizations;

CREATE TABLE IF NOT EXISTS public.organizations
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    name character varying COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT organizations_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.organizations
    OWNER to postgres;

ALTER TABLE public.emploees_stocks
    ADD CONSTRAINT emploees_stocks_emploee_id_fkey FOREIGN KEY (emploee_id)
        REFERENCES public.emploees (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE;
ALTER TABLE public.emploees_stocks
    ADD CONSTRAINT emploees_stocks_stock_id_fkey FOREIGN KEY (stock_id)
        REFERENCES public.stocks (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE;
ALTER TABLE public.items
    ADD CONSTRAINT "items_point of departure_fkey" FOREIGN KEY ("point of departure")
        REFERENCES public.countries (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID;

ALTER TABLE public.items
    ADD CONSTRAINT items_stock_fkey FOREIGN KEY (stock)
        REFERENCES public.stocks (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID;

ALTER TABLE public.items
    ADD CONSTRAINT items_type_fkey FOREIGN KEY (type)
        REFERENCES public.types (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID;

ALTER TABLE public.emploees
    ADD CONSTRAINT emploees_position_fkey FOREIGN KEY ("position")
        REFERENCES public.positions (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID;
ALTER TABLE public.emploees
    ADD CONSTRAINT emploees_priority_fkey FOREIGN KEY (priority)
        REFERENCES public.priorities (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID;

ALTER TABLE public.places
    ADD CONSTRAINT "Places_Country_fkey" FOREIGN KEY ("Country")
        REFERENCES public.countries (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE;
ALTER TABLE public.places
    ADD CONSTRAINT "places_Organization_fkey" FOREIGN KEY ("Organization")
        REFERENCES public.organizations (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE
        NOT VALID;

ALTER TABLE public.stocks
    ADD CONSTRAINT stocks_country_fkey FOREIGN KEY (country)
        REFERENCES public.countries (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE CASCADE;

-- Index: position

DROP INDEX IF EXISTS public."position";

CREATE INDEX  "position"
    ON public.emploees USING btree
    ("position" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: priority

DROP INDEX IF EXISTS public.priority;

CREATE INDEX  priority
    ON public.emploees USING btree
    (priority ASC NULLS LAST)
    TABLESPACE pg_default;

-- Index: emploee_id

DROP INDEX IF EXISTS public.emploee_id;

CREATE INDEX  emploee_id
    ON public.emploees_stocks USING btree
    (emploee_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: stock_id

DROP INDEX IF EXISTS public.stock_id;

CREATE INDEX  stock_id
    ON public.emploees_stocks USING btree
    (stock_id ASC NULLS LAST)
    TABLESPACE pg_default;

-- Index: point of departure

DROP INDEX IF EXISTS public."point of departure";

CREATE INDEX  "point of departure"
    ON public.items USING btree
    ("point of departure" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: stock

DROP INDEX IF EXISTS public.stock;

CREATE INDEX  stock
    ON public.items USING btree
    (stock ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: type

DROP INDEX IF EXISTS public.type;

CREATE INDEX  type
    ON public.items USING btree
    (type ASC NULLS LAST)
    TABLESPACE pg_default;


-- Index: country

DROP INDEX IF EXISTS public.country;

CREATE INDEX IF NOT EXISTS country
    ON public.places USING btree
    ("Country" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: organization

DROP INDEX IF EXISTS public.organization;

CREATE INDEX IF NOT EXISTS organization
    ON public.places USING btree
    ("Organization" ASC NULLS LAST)
    TABLESPACE pg_default;