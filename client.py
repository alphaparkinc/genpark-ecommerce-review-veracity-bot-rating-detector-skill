class EcommerceReviewVeracityBotRatingDetectorClient:
    def audit_product_reviews_veracity(self, product_page_url='https://retailer.com/dp/B09X4918', total_reviews_crawled_count=450):
        return {
            'review_audit_id': 'rvw_ver_8812',
            'product_url': product_page_url,
            'adjusted_true_rating_score': 3.8,
            'synthetic_bot_review_ratio_pct': 28.4,
            'seller_incentivized_review_detected': True,
            'veracity_grade_letter': 'C_PLUS',
            'review_authenticity_breakdown_url': 'https://veracity.commerce.genpark.ai/audits/8812.json'
        }
