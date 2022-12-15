class HTMLCreator():
    @staticmethod
    def create_html(bikes_data):
        html = """
        <!DOCTYPE html>
        <html>
        <body style="font-family: sans-serif; color: #222; margin: 0">
            <main
            style="
                max-width: 1000px;
                margin-left: auto;
                margin-right: auto;
                padding: 24px;
            "
            >
            <h2 style="margin: 0 0 0.35em; font-size: 28px">DJ Bikes</h2>
            <section style="display: flex; flex-wrap: wrap; padding-left: 0">
        """
        for index, bike in enumerate(bikes_data):
            if index != 0 and index % 4 == 0:
                html += "<br />"
            html += """
                <article
                style="
                    padding: 20px;
                    border: 1px solid #c9c9c9;
                    border-radius: 7px;
                    box-shadow: 2px 2px 4px rgba(0, 0, 0, 0.15);
                    flex: 0 0 25%;
                    margin: 0 15px 15px 0;
                "
                >
                <center>
                    <img
                    style="
                        border-radius: 7px 7px 0 0;
                        margin-bottom: 20px;
                        max-width: 100%;
                        height: auto;
                    "
                    src="{img}"
                    alt="{bike}"
                    />
                </center>
                <h3
                    style="
                    margin: 0 0 0.35em;
                    font-size: 28px;
                    color: rebeccapurple;
                    display: grid;
                    grid-template-columns: 1fr auto;
                    align-items: start;
                    "
                >
                    {bike}
                </h3>
                <h3
                    style="
                    margin: 0 0 0.35em;
                    font-size: 28px;
                    color: rebeccapurple;
                    display: grid;
                    grid-template-columns: 1fr auto;
                    align-items: start;
                    "
                >
                    <em
                    style="
                        padding: 0.25em;
                        background-color: #eddbff;
                        border-radius: 4px;
                    "
                    ><del style="color: crimson">{oldPrice}</del> {price}</em
                    >
                </h3>
                """.format(**bike)
            if bike.get("discount"):
                html += """
                <h4
                    style="
                    margin: 0 0 0.35em;
                    font-size: 16px;
                    color: rebeccapurple;
                    display: grid;
                    grid-template-columns: 1fr auto;
                    align-items: start;
                    "
                >
                    Save {discount}
                </h4>
                """.format(**bike)

            html += """<h4
                    style="
                    margin: 0 0 0.35em;
                    font-size: 16px;
                    color: rebeccapurple;
                    display: grid;
                    grid-template-columns: 1fr auto;
                    align-items: start;
                    "
                >
                    {store}
                </h4>
                <p style="margin: 0 0 1.15em; color: #757575; line-height: 1.5">
                    excl. VAT and shipping
                </p>
                <a
                    href="{url}"
                    style="
                    text-decoration: none;
                    background-color: rebeccapurple;
                    color: #fff;
                    padding: 0.5em 1em;
                    border-radius: 4px;
                    display: inline-block;
                    "
                    >Go To Store</a
                >
                </article>
                """.format(**bike)
        html += """
              </section>
            </main>
          </body>
        </html>
        """
        return html
