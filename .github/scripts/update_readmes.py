from datetime import datetime

import util


def main():
    listings = util.getListingsFromJSON()

    util.checkSchema(listings)
    listings = util.customFilter(listings)
    filtered = util.filterListings(listings, earliest_date=1714528377)
    
    util.sortListings(filtered)
    util.embedTable(filtered)

    util.setOutput("commit_message", "Updating README at " + datetime.now().strftime("%B %d, %Y %H:%M:%S"))


if __name__ == "__main__":
    main()
