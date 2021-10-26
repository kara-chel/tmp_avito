# tmp_avito

Небольшой пример парсинга сайта Авито на scrapy.
(Бесполезный скрипт) :)

```shell
2021-10-25 22:57:38 [scrapy.utils.log] INFO: Scrapy 2.5.1 started (bot: avito)
2021-10-25 22:57:38 [scrapy.utils.log] INFO: Versions: lxml 4.6.3.0, libxml2 2.9.10, cssselect 1.1.0, parsel 1.6.0, w3lib 1.22.0, Twisted 21.7.0, Python 3.7.3 (default, Jan 22 2021, 20:04:44) - [GCC 8.3.0], pyOpenSSL 21.0.0 (OpenSSL 1.1.1l  24 Aug 2021), cryptography 35.0.0, Platform Linux-5.8.0-0.bpo.2-amd64-x86_64-with-LinuxMint-4-debbie
2021-10-25 22:57:38 [scrapy.utils.log] DEBUG: Using reactor: twisted.internet.epollreactor.EPollReactor
2021-10-25 22:57:38 [scrapy.crawler] INFO: Overridden settings:
{'BOT_NAME': 'avito',
 'CONCURRENT_REQUESTS': 1,
 'CONCURRENT_REQUESTS_PER_DOMAIN': 1,
 'CONCURRENT_REQUESTS_PER_IP': 1,
 'DOWNLOAD_DELAY': 3,
 'NEWSPIDER_MODULE': 'avito.spiders',
 'SPIDER_MODULES': ['avito.spiders'],
 'USER_AGENT': 'Mozilla/5.0 (X11; Linux x86_64; rv:78.0) Gecko/20100101 '
               'Firefox/78.0'}
2021-10-25 22:57:38 [scrapy.extensions.telnet] INFO: Telnet Password: 11a73c669a3584d8
2021-10-25 22:57:38 [scrapy.middleware] INFO: Enabled extensions:
['scrapy.extensions.corestats.CoreStats',
 'scrapy.extensions.telnet.TelnetConsole',
 'scrapy.extensions.memusage.MemoryUsage',
 'scrapy.extensions.logstats.LogStats']
2021-10-25 22:57:38 [scrapy.middleware] INFO: Enabled downloader middlewares:
['scrapy.downloadermiddlewares.httpauth.HttpAuthMiddleware',
 'scrapy.downloadermiddlewares.downloadtimeout.DownloadTimeoutMiddleware',
 'scrapy.downloadermiddlewares.defaultheaders.DefaultHeadersMiddleware',
 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware',
 'scrapy.downloadermiddlewares.retry.RetryMiddleware',
 'scrapy.downloadermiddlewares.redirect.MetaRefreshMiddleware',
 'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware',
 'scrapy.downloadermiddlewares.redirect.RedirectMiddleware',
 'scrapy.downloadermiddlewares.cookies.CookiesMiddleware',
 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware',
 'scrapy.downloadermiddlewares.stats.DownloaderStats']
2021-10-25 22:57:38 [scrapy.middleware] INFO: Enabled spider middlewares:
['scrapy.spidermiddlewares.httperror.HttpErrorMiddleware',
 'scrapy.spidermiddlewares.offsite.OffsiteMiddleware',
 'scrapy.spidermiddlewares.referer.RefererMiddleware',
 'scrapy.spidermiddlewares.urllength.UrlLengthMiddleware',
 'scrapy.spidermiddlewares.depth.DepthMiddleware']
2021-10-25 22:57:38 [scrapy.middleware] INFO: Enabled item pipelines:
[]
2021-10-25 22:57:38 [scrapy.core.engine] INFO: Spider opened
2021-10-25 22:57:38 [scrapy.extensions.logstats] INFO: Crawled 0 pages (at 0 pages/min), scraped 0 items (at 0 items/min)
2021-10-25 22:57:38 [scrapy.extensions.telnet] INFO: Telnet console listening on 127.0.0.1:6023
2021-10-25 22:57:39 [scrapy.downloadermiddlewares.redirect] DEBUG: Redirecting (301) to <GET https://www.avito.ru/> from <GET https://avito.ru/>
2021-10-25 22:57:43 [scrapy.core.engine] DEBUG: Crawled (200) <GET https://www.avito.ru/> (referer: None)
{'title': 'Лошадь', 'url': 'https://www.avito.ru/chelyabinsk/drugie_zhivotnye/loshad_2246308549'}
{'title': '1-к. квартира, 35,5\xa0м², 10/10\xa0эт.', 'url': 'https://www.avito.ru/chelyabinsk/kvartiry/1-k._kvartira_355m_1010et._2254190528'}
{'title': 'Прицеп Спутник Zn 2513/37 тент 1550', 'url': 'https://www.avito.ru/chelyabinsk/zapchasti_i_aksessuary/pritsep_sputnik_zn_251337_tent_1550_2247738184'}
{'title': '1-к. квартира, 40,4\xa0м², 6/10\xa0эт.', 'url': 'https://www.avito.ru/chelyabinsk/kvartiry/1-k._kvartira_404m_610et._2264055582'}
{'title': 'Квартира-студия, 43\xa0м², 2/10\xa0эт.', 'url': 'https://www.avito.ru/chelyabinsk/kvartiry/kvartira-studiya_43m_210et._2240594379'}
{'title': 'Nissan Lafesta, 2008', 'url': 'https://www.avito.ru/chelyabinsk/avtomobili/nissan_lafesta_2008_2256916932'}
{'title': 'Водитель такси подработка на своем авто', 'url': 'https://www.avito.ru/chelyabinsk/vakansii/voditel_taksi_podrabotka_na_svoem_avto_2245321557'}
{'title': 'Домашний хорек', 'url': 'https://www.avito.ru/chelyabinsk/drugie_zhivotnye/domashniy_horek_2264868050'}
{'title': 'Защитная маска для лица', 'url': 'https://www.avito.ru/chelyabinsk/krasota_i_zdorove/zaschitnaya_maska_dlya_litsa_2257337345'}
{'title': 'Восстановление эмали ванн', 'url': 'https://www.avito.ru/chelyabinsk/predlozheniya_uslug/vosstanovlenie_emali_vann_2242595377'}
{'title': 'Колеса на квадроцикл BRP', 'url': 'https://www.avito.ru/chelyabinsk/zapchasti_i_aksessuary/kolesa_na_kvadrotsikl_brp_2256455172'}
{'title': 'Спортивный комплекс Челябинск', 'url': 'https://www.avito.ru/chelyabinsk/kommercheskaya_nedvizhimost/sportivnyy_kompleks_chelyabinsk_2258998630'}
{'title': 'Рюкзак Among as', 'url': 'https://www.avito.ru/chelyabinsk/odezhda_obuv_aksessuary/ryukzak_among_as_2263313695'}
{'title': 'Джемпер Modis S 44', 'url': 'https://www.avito.ru/chelyabinsk/odezhda_obuv_aksessuary/dzhemper_modis_s_44_2110152614'}
{'title': 'Комбинезон Remu Travalle', 'url': 'https://www.avito.ru/chelyabinsk/detskaya_odezhda_i_obuv/kombinezon_remu_travalle_2025006703'}
{'title': 'Гель-лак, наращивание', 'url': 'https://www.avito.ru/chelyabinsk/predlozheniya_uslug/gel-lak_naraschivanie_2253329003'}
{'title': 'Зимняя резина r13 липучка', 'url': 'https://www.avito.ru/chelyabinsk/zapchasti_i_aksessuary/zimnyaya_rezina_r13_lipuchka_2268662494'}
{'title': 'Видеокарта', 'url': 'https://www.avito.ru/chelyabinsk/tovary_dlya_kompyutera/videokarta_2245969783'}
{'title': '2-к. квартира, 57,3\xa0м², 8/8\xa0эт.', 'url': 'https://www.avito.ru/chelyabinsk/kvartiry/2-k._kvartira_573m_88et._2252654699'}
{'title': '1-к. квартира, 31\xa0м², 1/5\xa0эт.', 'url': 'https://www.avito.ru/chelyabinsk/kvartiry/1-k._kvartira_31m_15et._2267912344'}
{'title': 'Бейсбольная бита', 'url': 'https://www.avito.ru/chelyabinsk/sport_i_otdyh/beysbolnaya_bita_2245593474'}
{'title': 'Участок 6,7 сот. (СНТ, ДНП)', 'url': 'https://www.avito.ru/chelyabinsk/zemelnye_uchastki/uchastok_67_sot._snt_dnp_2261375648'}
{'title': 'Шины 225 45 р17 Bridgestone Blizzak Revo', 'url': 'https://www.avito.ru/chelyabinsk/zapchasti_i_aksessuary/shiny_225_45_r17_bridgestone_blizzak_revo_2243758381'}
{'title': 'Стол лофт "Birch" из дерева (береза)', 'url': 'https://www.avito.ru/chelyabinsk/mebel_i_interer/stol_loft_birch_iz_dereva_bereza_2248382837'}
{'title': 'Лошади', 'url': 'https://www.avito.ru/chelyabinsk/drugie_zhivotnye/loshadi_2266099508'}
{'title': '1-к. квартира, 43\xa0м², 8/10\xa0эт.', 'url': 'https://www.avito.ru/chelyabinsk/kvartiry/1-k._kvartira_43m_810et._2262627499'}
{'title': 'Бетонщик-арматурщик с проживанием и питанием', 'url': 'https://www.avito.ru/chelyabinsk/vakansii/betonschik-armaturschik_s_prozhivaniem_i_pitaniem_2273869118'}
{'title': 'Курганский прицеп "Крепыш"', 'url': 'https://www.avito.ru/chelyabinsk/zapchasti_i_aksessuary/kurganskiy_pritsep_krepysh_2247818657'}
{'title': '1-к. квартира, 41 м², 10/11 эт.', 'url': 'https://www.avito.ru/chelyabinsk/kvartiry/1-k._kvartira_41_m_1011_et._2243747113'}
2021-10-25 22:57:43 [scrapy.core.engine] INFO: Closing spider (finished)
2021-10-25 22:57:43 [scrapy.statscollectors] INFO: Dumping Scrapy stats:
{'downloader/request_bytes': 488,
 'downloader/request_count': 2,
 'downloader/request_method_count/GET': 2,
 'downloader/response_bytes': 130870,
 'downloader/response_count': 2,
 'downloader/response_status_count/200': 1,
 'downloader/response_status_count/301': 1,
 'elapsed_time_seconds': 4.613604,
 'finish_reason': 'finished',
 'finish_time': datetime.datetime(2021, 10, 25, 17, 57, 43, 564135),
 'httpcompression/response_bytes': 819193,
 'httpcompression/response_count': 1,
 'log_count/DEBUG': 2,
 'log_count/INFO': 10,
 'memusage/max': 1596403712,
 'memusage/startup': 1596403712,
 'response_received_count': 1,
 'scheduler/dequeued': 2,
 'scheduler/dequeued/memory': 2,
 'scheduler/enqueued': 2,
 'scheduler/enqueued/memory': 2,
 'start_time': datetime.datetime(2021, 10, 25, 17, 57, 38, 950531)}
2021-10-25 22:57:43 [scrapy.core.engine] INFO: Spider closed (finished)

Process finished with exit code 0

```
