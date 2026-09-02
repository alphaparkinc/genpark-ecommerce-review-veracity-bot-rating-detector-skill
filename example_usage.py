from client import EcommerceReviewVeracityBotRatingDetectorClient

def main():
    client = EcommerceReviewVeracityBotRatingDetectorClient()
    res = client.audit_product_reviews_veracity('https://shop.com/item/4918', 600)
    print('Review Veracity Detector: ' + res['review_audit_id'] + ' (Grade: ' + res['veracity_grade_letter'] + ')')
    print('Adjusted Rating: ' + str(res['adjusted_true_rating_score']) + ' / 5.0 | Synthetic Ratio: ' + str(res['synthetic_bot_review_ratio_pct']) + '%')
    print('Breakdown URL: ' + res['review_authenticity_breakdown_url'])

if __name__ == '__main__':
    main()
