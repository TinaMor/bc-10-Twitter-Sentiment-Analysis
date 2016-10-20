import main_utilities
import sys
import os
try:
    main_utilities.main_loop()
except KeyboardInterrupt:
    print('Twitter Sentiment Analysis was rudely interrupted!!')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)

