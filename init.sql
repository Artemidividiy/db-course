-- Table: public.countries
DROP TABLE IF EXISTS public.countries CASCADE;

CREATE TABLE IF NOT EXISTS public.countries
(
    id integer NOT NULL,
    name VARCHAR NOT NULL,
    CONSTRAINT countries_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.countries
    OWNER to postgres;

-- Table: public.emploees

DROP TABLE IF EXISTS public.emploees CASCADE;

CREATE TABLE IF NOT EXISTS public.emploees
(
    id integer NOT NULL,
    name VARCHAR NOT NULL,
    "position" integer NOT NULL,
    "birth year" date NOT NULL,
    priority integer NOT NULL,
    CONSTRAINT emploee_pkey PRIMARY KEY (id),
    CONSTRAINT emploees_position_fkey FOREIGN KEY ("position")
        REFERENCES public.positions (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT emploees_priority_fkey FOREIGN KEY (priority)
        REFERENCES public.priorities (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.emploees
    OWNER to postgres;
-- Index: position

DROP INDEX IF EXISTS public."position";

CREATE INDEX IF NOT EXISTS "position"
    ON public.emploees USING btree
    ("position" ASC NULLS LAST)
    TABLESPACE pg_default;

-- Table: public.emploees_stocks

DROP TABLE IF EXISTS public.emploees_stocks CASCADE;

CREATE TABLE IF NOT EXISTS public.emploees_stocks
(
    id integer NOT NULL,
    stock_id integer NOT NULL,
    emploee_id integer NOT NULL,
    CONSTRAINT emploees_stocks_pkey PRIMARY KEY (id),
    CONSTRAINT emploees_stocks_emploee_id_fkey FOREIGN KEY (emploee_id)
        REFERENCES public.emploees (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT emploees_stocks_stock_id_fkey FOREIGN KEY (stock_id)
        REFERENCES public.stocks (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.emploees_stocks
    OWNER to postgres;
-- Index: emploee

DROP INDEX IF EXISTS public.emploee CASCADE;

CREATE INDEX IF NOT EXISTS emploee
    ON public.emploees_stocks USING btree
    (emploee_id ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: emploee_id

DROP INDEX IF EXISTS public.emploee_id;

CREATE INDEX IF NOT EXISTS emploee_id
    ON public.emploees_stocks USING btree
    (emploee_id ASC NULLS LAST)
    TABLESPACE pg_default;

-- Table: public.items

DROP TABLE IF EXISTS public.items CASCADE;

CREATE TABLE IF NOT EXISTS public.items
(
    id integer NOT NULL,
    type integer NOT NULL,
    stock integer NOT NULL,
    name VARCHAR NOT NULL,
    arrival_time time without time zone NOT NULL,
    arrival_date date NOT NULL,
    "point of departure" integer NOT NULL,
    CONSTRAINT items_pkey PRIMARY KEY (id),
    CONSTRAINT items_point_of_departure FOREIGN KEY ("point of departure")
        REFERENCES public.places (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT items_stock_fkey FOREIGN KEY (stock)
        REFERENCES public.stocks (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT items_stock_fkey1 FOREIGN KEY (stock)
        REFERENCES public.stocks (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT items_type_fkey FOREIGN KEY (type)
        REFERENCES public.types (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.items
    OWNER to postgres;
-- Index: stock

DROP INDEX IF EXISTS public.stock;

CREATE INDEX IF NOT EXISTS stock
    ON public.items USING btree
    (stock ASC NULLS LAST)
    TABLESPACE pg_default;
-- Index: type

DROP INDEX IF EXISTS public.type;

CREATE INDEX IF NOT EXISTS type
    ON public.items USING btree
    (type ASC NULLS LAST)
    TABLESPACE pg_default;

-- Table: public.places

DROP TABLE IF EXISTS public.places CASCADE;

CREATE TABLE IF NOT EXISTS public.places
(
    id integer NOT NULL,
    "Name" VARCHAR NOT NULL,
    "Organization" integer,
    longitude double precision NOT NULL,
    latitude double precision NOT NULL,
    "Country" integer NOT NULL,
    CONSTRAINT "Places_pkey" PRIMARY KEY (id),
    CONSTRAINT "Places_Country_fkey" FOREIGN KEY ("Country")
        REFERENCES public.countries (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.places
    OWNER to postgres;
-- Index: country

DROP INDEX IF EXISTS public.country;

CREATE INDEX IF NOT EXISTS country
    ON public.places USING btree
    ("Country" ASC NULLS LAST)
    TABLESPACE pg_default;
-- Table: public.positions

DROP TABLE IF EXISTS public.positions CASCADE;

CREATE TABLE IF NOT EXISTS public.positions
(
    id integer NOT NULL,
    name VARCHAR NOT NULL,
    CONSTRAINT positions_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.positions
    OWNER to postgres;
-- Table: public.priorities

DROP TABLE IF EXISTS public.priorities CASCADE;

CREATE TABLE IF NOT EXISTS public.priorities
(
    id integer NOT NULL,
    "number" integer NOT NULL,
    CONSTRAINT priority_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.priorities
    OWNER to postgres;
-- Table: public.stocks

DROP TABLE IF EXISTS public.stocks CASCADE;

CREATE TABLE IF NOT EXISTS public.stocks
(
    id integer NOT NULL,
    name VARCHAR,
    longitude double precision NOT NULL,
    latitude double precision NOT NULL,
    country integer NOT NULL,
    CONSTRAINT stocks_pkey PRIMARY KEY (id),
    CONSTRAINT stocks_country_fkey FOREIGN KEY (country)
        REFERENCES public.countries (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.stocks
    OWNER to postgres;

-- Table: public.types

DROP TABLE IF EXISTS public.types CASCADE;

CREATE TABLE IF NOT EXISTS public.types
(
    id integer NOT NULL,
    name VARCHAR NOT NULL,
    CONSTRAINT types_pkey PRIMARY KEY (id)
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.types
    OWNER to postgres;