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
                    {store}
                </h4>
                """.format(**bike)

            if bike.get("stock"):
                html += """
                <p
                    style="
                    border: 2px solid #228b22;
                    border-radius: 5px;
                    color: #228b22;
                    padding: 7px 14px;
                    font-size: 16px;
                    width: 7em;
                    "
                >
                    <svg
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink"
                    viewBox="0,0,256,256"
                    width="20px"
                    height="20px"
                    fill-rule="nonzero"
                    >
                    <g
                        fill="#228b22"
                        fill-rule="nonzero"
                        stroke="none"
                        stroke-width="1"
                        stroke-linecap="butt"
                        stroke-linejoin="miter"
                        stroke-miterlimit="10"
                        stroke-dasharray=""
                        stroke-dashoffset="0"
                        font-family="none"
                        font-weight="none"
                        font-size="none"
                        text-anchor="none"
                        style="mix-blend-mode: normal"
                    >
                        <g transform="scale(10.66667,10.66667)">
                        <path
                            d="M12,2c-5.514,0 -10,4.486 -10,10c0,5.514 4.486,10 10,10c5.514,0 10,-4.486 10,-10c0,-1.126 -0.19602,-2.2058 -0.54102,-3.2168l-1.61914,1.61914c0.105,0.516 0.16016,1.05066 0.16016,1.59766c0,4.411 -3.589,8 -8,8c-4.411,0 -8,-3.589 -8,-8c0,-4.411 3.589,-8 8,-8c1.633,0 3.15192,0.49389 4.41992,1.33789l1.43164,-1.43164c-1.648,-1.194 -3.66656,-1.90625 -5.85156,-1.90625zM21.29297,3.29297l-10.29297,10.29297l-3.29297,-3.29297l-1.41406,1.41406l4.70703,4.70703l11.70703,-11.70703z"
                        />
                        </g>
                    </g>
                    </svg>
                    <b>In Stock</b>
                </p>
            """
            else:
                html += """
                <p
                    style="
                    border: 2px solid #ee4b2b;
                    border-radius: 5px;
                    color: #ee4b2b;
                    padding: 7px 14px;
                    font-size: 16px;
                    width: 9em;
                    "
                >
                    <svg
                    xmlns="http://www.w3.org/2000/svg"
                    xmlns:xlink="http://www.w3.org/1999/xlink"
                    viewBox="0,0,256,256"
                    width="20px"
                    height="20px"
                    fill-rule="nonzero"
                    >
                    <g
                        fill="#ee4b2b"
                        fill-rule="nonzero"
                        stroke="none"
                        stroke-width="1"
                        stroke-linecap="butt"
                        stroke-linejoin="miter"
                        stroke-miterlimit="10"
                        stroke-dasharray=""
                        stroke-dashoffset="0"
                        font-family="none"
                        font-weight="none"
                        font-size="none"
                        text-anchor="none"
                        style="mix-blend-mode: normal"
                    >
                        <g transform="scale(10.66667,10.66667)">
                        <path
                            d="M4.70703,3.29297l-1.41406,1.41406l7.29297,7.29297l-7.29297,7.29297l1.41406,1.41406l7.29297,-7.29297l7.29297,7.29297l1.41406,-1.41406l-7.29297,-7.29297l7.29297,-7.29297l-1.41406,-1.41406l-7.29297,7.29297z"
                        />
                        </g>
                    </g>
                    </svg>
                    <b>Out Of Stock</b>
                </p>
                """

            html += """
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
